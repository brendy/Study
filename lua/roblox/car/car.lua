local FR = script.Parent.Parent.Fr
local FL = script.Parent.Parent.Fl
local BL = script.Parent.Parent.Bl
local BR = script.Parent.Parent.Br
local steer = script.Parent.Parent.Steer

local Speed = 50 -- 원하는 속도
local Angle = 15 -- 원하는 앵글 각도

script.Parent.Changed:Connect(function(property)
 	FR.AngularVelocity = Speed * -script.Parent.Throttle
 	BR.AngularVelocity = Speed * -script.Parent.Throttle
 	FL.AngularVelocity = Speed * script.Parent.Throttle
 	BL.AngularVelocity = Speed * script.Parent.Throttle
 	steer.TargetAngle = Angle * script.Parent.Steer
end)